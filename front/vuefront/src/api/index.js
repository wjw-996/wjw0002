import axios from "axios"
import jsCookie from 'js-cookie'

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
	config.headers.Authorization = `Bearer ${jsCookie.get("access")}`
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
  }, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
  });




export const getCategoryList = ()=>{

	return axios.get("api/v1/categorys/")
}

export const createCategory = (param)=>{
	return axios.post("api/v1/categorys/",param)
}

export const getToken = (param)=>{
	return axios.post("login1/",param,)
}

export const updateCategory = (param)=>{
	return axios.put(`api/v1/categorys/${param.id}/`,param)
}