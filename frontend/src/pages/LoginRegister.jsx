import React, { useState } from "react";
import "../styles/LoginRegister.css";
import InputBox from "../components/InputBox";
import TogglePanel from "../components/TogglePanel";
import { login, register } from "../services/authService";

const LoginRegister = () => {
  const [active, setActive] = useState(false);
  const [formData, setFormData] = useState({});

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const token = await login(formData.correo, formData.contrasena);
      alert("Inicio de sesión exitoso ✅");
      console.log("Token:", token);
    } catch (error) {
      alert("Error al iniciar sesión ❌");
      console.error(error);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const token = await register(formData);
      alert("Registro exitoso ✅");
      console.log("Token:", token);
    } catch (error) {
      alert("Error al registrar ❌");
      console.error(error);
    }
  };

  return (
    <div className={`container ${active ? "active" : ""}`}>
      {/* LOGIN */}
      <div className="form-box login">
        <form onSubmit={handleLogin}>
          <h1>Inicia sesión</h1>
          <InputBox name="correo" type="email" placeholder="Correo electrónico"
            icon="bx bxs-envelope"
            onChange={handleChange}
          />
          <InputBox
            name="contrasena"
            type="password"
            placeholder="Contraseña"
            icon="bx bxs-lock-alt"
            onChange={handleChange}
          />
          <div className="forget-link">
            <a href="#">¿Olvidaste tu contraseña?</a>
          </div>
          <button type="submit" className="btn">Iniciar sesión</button>
        </form>
      </div>

      {/* REGISTER */}
      <div className="form-box register">
        <form onSubmit={handleRegister}>
          <h1>Registro</h1>
          <InputBox
            name="num_documento"
            type="text"
            placeholder="Número de documento"
            icon="bx bxs-user"
            onChange={handleChange}
          />

          <InputBox icon="bx bxs-id-card">
            <select name="tipo_documento" onChange={handleChange} required>
              <option value="" disabled selected>
                Tipo de documento
              </option>
              <option value="CC">Cédula de ciudadanía</option>
              <option value="TI">Tarjeta de identidad</option>
              <option value="PAS">Cédula de extranjería</option>
            </select>
          </InputBox>

          <InputBox name="nombre" type="text" placeholder="Nombres" icon="bx bxs-user" onChange={handleChange}/>
          <InputBox name="apellido" type="text" placeholder="Apellidos" icon="bx bxs-user" onChange={handleChange}/>
          <InputBox name="telefono" type="tel" placeholder="Teléfono" icon="bx bxs-phone" onChange={handleChange}/>
          
          <InputBox icon="bx bxs-id-card">
            <select name="genero" onChange={handleChange} required>
              <option value="" disabled selected>
                Genero
              </option>
              <option value="Masculino">Masculino</option>
              <option value="Femenino">Femenino</option>
            </select>
          </InputBox>
          <InputBox name="direccion" type="text" placeholder="Dirección" icon="bx bxs-home" onChange={handleChange} />
          <InputBox name="correo" type="email" placeholder="Correo" icon="bx bxs-envelope" onChange={handleChange} />
          <InputBox name="contrasena" type="password" placeholder="Contraseña" icon="bx bxs-lock-alt" onChange={handleChange} />
          <InputBox name="fecha_nacimiento" type="date" placeholder="Fecha de nacimiento" icon="bx bxs-calendar" onChange={handleChange} />

          <button type="submit" className="btn">Registrar</button>
        </form>
      </div>

      {/* TOGGLE */}
      <div className="toggle-box">
        <TogglePanel title="Hola, Bienvenidos!" text="¿No tienes una cuenta?" buttonText="Registrar" onClick={() => setActive(true)} position="toggle-left" />
        <TogglePanel title="¡Bienvenido de nuevo!" text="¿Ya tienes una cuenta?" buttonText="Inicia sesión" onClick={() => setActive(false)} position="toggle-right" />
      </div>
    </div>
  );
};

export default LoginRegister;
