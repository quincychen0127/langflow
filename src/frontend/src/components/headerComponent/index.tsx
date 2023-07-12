import { Home, MoonIcon, SunIcon, Users2 } from "lucide-react";
import { useContext, useEffect, useState } from "react";
import { FaDiscord, FaGithub, FaTwitter } from "react-icons/fa";
import { Button } from "../ui/button";
import { TabsContext } from "../../contexts/tabsContext";
import AlertDropdown from "../../alerts/alertDropDown";
import { alertContext } from "../../contexts/alertContext";
import { darkContext } from "../../contexts/darkContext";
import { PopUpContext } from "../../contexts/popUpContext";
import { typesContext } from "../../contexts/typesContext";
import MenuBar from "./components/menuBar";
import { Link, useLocation, useParams } from "react-router-dom";
import { USER_PROJECTS_HEADER } from "../../constants";
import { getRepoStars } from "../../controllers/API";
import { Separator } from "../ui/separator";
import { Bell } from "lucide-react";

export default function Header() {
  const { flows, addFlow, tabId } = useContext(TabsContext);
  const { openPopUp } = useContext(PopUpContext);
  const { templates } = useContext(typesContext);
  const { id } = useParams();
  const AlertWidth = 384;
  const { dark, setDark } = useContext(darkContext);
  const { notificationCenter, setNotificationCenter, setErrorData } =
    useContext(alertContext);
  const location = useLocation();

  const [stars, setStars] = useState(null);

  useEffect(() => {
    async function fetchStars() {
      const starsCount = await getRepoStars("logspace-ai", "langflow");
      setStars(starsCount);
    }
    fetchStars();
    setDark(true);
  }, []);
  return (
    <div className="header-arrangement">
      <div className="header-start-display">
        <Link to="/">
          <span className="ml-4 text-2xl">⛓️</span>
        </Link>
        {flows.findIndex((f) => tabId === f.id) !== -1 && tabId !== "" && (
          <MenuBar flows={flows} tabId={tabId} />
        )}
      </div>
    
      
      <div style={{
        color: "white",
        fontFamily: "Monoton",
        textTransform: "uppercase",
        textShadow: "0 0 60px #ffffff,0 0 30px #009000,0 0 5px #0000ff",
        backgroundColor: "#131516",
        borderRadius: "10%",
        padding: "15px",
        borderColor: "rgb(126, 117, 103)",
        borderWidth: "1px",
        marginTop: "40px",
        whiteSpace: "nowrap",
        zIndex: "10",
      }}>
        <h1 className = "text-7xl">007 WORKBENCH</h1>
      </div>

      <div className="header-end-division">
      </div>
    </div>
  );
}
