import axios from 'axios'

const user = typeof window !== 'undefined' ? localStorage.getItem('current_user') : "";

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
    }
});
axiosInstance.interceptors.response.use(
    response => response,
    error => {
      const originalRequest = error.config;
      if (error?.response?.status === 401)  {
        const refresh_token = user.refresh_token;
        if (refresh_token !== "undefined") {
        return axiosInstance
              .post('/refresh-token/', {refresh: refresh_token})
              .then((response) => {
                  user.access_token = response.data.access;
                  user.refresh_token = response.data.refresh;
                  localStorage.setItem('current_user', storedUser);
                  axiosInstance.defaults.headers['Authorization'] = "Bearer " + response.data.access;
                  originalRequest.headers['Authorization'] = "Bearer " + response.data.access;

                  return axiosInstance(originalRequest);
              })
              .catch(err => {
                  console.log(err)
              });
            }
      }
    
      return Promise.reject(error);
      }

);

export default axiosInstance
