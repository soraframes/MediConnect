import React from "react";

const InputBox = ({ type, placeholder, icon, children, ...props }) => {
  return (
    <div className="input-box">
      {children ? (
        children
      ) : (
        <input type={type} placeholder={placeholder} required {...props} />
      )}
      <i className={icon}></i>
    </div>
  );
};

export default InputBox;
