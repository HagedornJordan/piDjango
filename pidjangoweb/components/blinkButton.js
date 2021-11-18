import ToolCard from "./toolCard";
import axiosInstance from "../helpers/axios";

function sendBlink() {
    axiosInstance.request({
        url: "http://127.0.0.1:8000/blink/?pin=23&blinks=5&pause=.25",
        method: "get",
      }).then((res) => {
        console.log(res);
      });
}

const BlinkButton = (props) => {
return (
    <ToolCard>
      <div className="flex-1">
        <div className="flex justify-center">
          <button onClick={sendBlink} > BLINK! </button>
        </div>
      </div>
    </ToolCard>
  );
};

export default BlinkButton;
