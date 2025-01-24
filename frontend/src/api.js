import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

//const apiUrl = "/choreo-apis/personalwebsite/backend/v1.0";
const apiUrl = "https://localhost:8000";
//const apiUrl = "ec2-3-129-6-154.us-east-2.compute.amazonaws.com/";
//const apiUrl = "http://ec2-3-129-6-154.us-east-2.compute.amazonaws.com";

console.log("HERE");

const api = axios.create({
  baseURL: apiUrl,
  /*baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,*/
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
