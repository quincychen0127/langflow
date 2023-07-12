import { useContext, useEffect, useState } from "react";
import { GithubIcon, Users2, GitFork } from "lucide-react";
import { TabsContext } from "../../contexts/tabsContext";
import { alertContext } from "../../contexts/alertContext";
import { Button } from "../../components/ui/button";

import { getExamples } from "../../controllers/API";
import { FlowType } from "../../types/flow";
import { CardComponent } from "../../components/cardComponent";
import { useNavigate } from "react-router-dom";
export default function CommunityPage() {
  const { flows, setTabId, downloadFlows, uploadFlows, addFlow } =
    useContext(TabsContext);
  useEffect(() => {
    setTabId("");
  }, []);
  const { setErrorData } = useContext(alertContext);
  const [loadingExamples, setLoadingExamples] = useState(false);
  const [examples, setExamples] = useState<FlowType[]>([]);
  function handleExamples() {
    setLoadingExamples(true);
    getExamples()
      .then((result) => {
        setLoadingExamples(false);
        setExamples(result);
      })
      .catch((error) =>
        setErrorData({
          title: "there was an error loading examples, please try again",
          list: [error.message],
        })
      );
  }
  const navigate = useNavigate();

  useEffect(() => {
    handleExamples();
  }, []);
  return (""
    
  );
}
