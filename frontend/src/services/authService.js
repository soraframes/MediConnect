import api from "./api";

export const login = async (correo, contrasena) => {
  const response = await api.post("/auth/login", {
    correo,
    contrasena,
  });
  const token = response.data.access_token;
  localStorage.setItem("token", token);
  return token;
};

export const register = async (user_data) => {
  const response = await api.post("/auth/register", user_data);
  const token = response.data.access_token;
  localStorage.setItem("token", token);
  return token;
};
