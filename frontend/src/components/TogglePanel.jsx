import React from "react";

const TogglePanel = ({ title, text, buttonText, onClick, position }) => {
  return (
    <div className={`toggle-panel ${position}`}>
      <h1>{title}</h1>
      <p>{text}</p>
      <button className="btn" onClick={onClick}>
        {buttonText}
      </button>
    </div>
  );
};

export default TogglePanel;
