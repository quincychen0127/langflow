import { ConnectionLineComponentProps } from "reactflow";

const ConnectionLineComponent = ({
  fromX,
  fromY,
  toX,
  toY,
  connectionLineStyle = {}, // provide a default value for connectionLineStyle
}: ConnectionLineComponentProps) => {
  return (
    <g>
      <path
        fill="none"
        // ! Replace hash # colors here
        stroke="#FFF"
        strokeWidth={1.5}
        className="animated "
        d={`M${fromX},${fromY} C ${fromX} ${toY} ${fromX} ${toY} ${toX},${toY}`}
        style={connectionLineStyle}
      />
      <circle
        cx={toX}
        cy={toY}
        fill="#fff"
        r={3}
        stroke="#222"
        className=""
        strokeWidth={1.5}
      />
    </g>
  );
};

export default ConnectionLineComponent;
