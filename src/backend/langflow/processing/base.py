from langflow.api.v1.callback import (
    AsyncStreamingLLMCallbackHandler,
    StreamingLLMCallbackHandler,
)
from langflow.processing.process import fix_memory_inputs, format_actions
from langflow.utils.logger import logger


async def get_result_and_steps(langchain_object, message: str, **kwargs):
    """Get result and thought from extracted json"""

    try:
        if hasattr(langchain_object, "verbose"):
            langchain_object.verbose = True
        chat_input = None
        memory_key = ""
        if hasattr(langchain_object, "memory") and langchain_object.memory is not None:
            memory_key = langchain_object.memory.memory_key

        if hasattr(langchain_object, "input_keys"):
            for key in langchain_object.input_keys:
                if key not in [memory_key, "chat_history"]:
                    chat_input = {key: message}
        else:
            chat_input = message  # type: ignore

        if hasattr(langchain_object, "return_intermediate_steps"):
            # https://github.com/hwchase17/langchain/issues/2068
            # Deactivating until we have a frontend solution
            # to display intermediate steps
            langchain_object.return_intermediate_steps = True

        fix_memory_inputs(langchain_object)

        #if hasattr(langchain_object, "agent"):
        #    chat_input['input'] = f"Can you make a plan for the following problem and execute it? Use the planner agent then execute its tasks. The problem is {chat_input['input']} Please use the tools you have to execute them as well. Write an email if asked."
        
        langchain_object.verbose = True

        try:
            async_callbacks = [AsyncStreamingLLMCallbackHandler(**kwargs)]
            output = await langchain_object.acall(chat_input, callbacks=async_callbacks)
        except Exception as exc:
            # make the error message more informative
            logger.debug(f"Error: {str(exc)}")
            sync_callbacks = [StreamingLLMCallbackHandler(**kwargs)]
            output = langchain_object(chat_input, callbacks=sync_callbacks)

        intermediate_steps = (
            output.get("intermediate_steps", []) if isinstance(output, dict) else []
        )

        output_strings = [output[key] for key in output.keys() if key != 'input']
        result = (
            # output.get(langchain_object.output_keys[0]) 
            '\n\n\n'.join(output_strings)
            if hasattr(langchain_object, "chains")
            else output.get(langchain_object.output_keys[0])
        )
        thought = format_actions(intermediate_steps) if intermediate_steps else ""
    except Exception as exc:
        logger.exception(exc)
        raise ValueError(f"Error: {str(exc)}") from exc
    return result, thought
