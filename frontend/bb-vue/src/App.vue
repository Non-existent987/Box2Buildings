<script setup>
import HelloWorld from './components/HelloWorld.vue';
import axios from 'axios';
import { ref } from 'vue';
// 数据属性被转换为引用
const backendMessage = ref(''); // 用于存储从后端获取的消息
const errorMessage = ref('');  // 用于存储请求错误信息
// 方法被转换为函数
const fetchData = async () => {
  // 清空之前的消息和错误
  backendMessage.value = '正在加载中......';
  errorMessage.value = '';
  try {
    // 发起 get 请求到后端
    const response = await axios.get('http://localhost:8000/hello/');
    backendMessage.value = response.data.message;
    console.error('获取数据成功：');
  } catch (error) {
    console.error('获取数据失败：', error);
    backendMessage.value = '获取数据失败。';
    if (error.response) {
      // 请求已发出，但服务器响应的状态码不在 2xx 范围内
      errorMessage.value = `服务器错误: ${error.response.status} - ${error.response.data?.message || error.response.statusText}`;
    } else if (error.request) {
      // 请求已发出，但没有收到响应
      errorMessage.value = '网络错误: 未收到服务器响应。请检查后端是否运行或网络连接。';
    } else {
      // 在设置请求时发生了一些事情，触发了一个错误
      errorMessage.value = `请求配置错误: ${error.message}`;
    }
  }
};
</script>

<template>
  <!--跟容器 -->
  <div class="app">
    <!-- 侧边栏内容，后续补充 -->
    <div class="sidebar">
      <h2>建筑物智能提取</h2>
      <p>切换模式</p>
      <div class="sidebar-buttons">
        
        <button class="sidebar-button-point">点选模式</button>
        <button class="sidebar-button-rectangle">框选模式</button>
      </div>
      <div class="sidebar-dropdown">
        <p>切换底图:</p>
        <select class="basemap-select">
          <option value="satellite" selected>卫星图</option>
          <option value="street">街道图</option>
        </select>
      </div>
      <!-- 测试下按钮和后端联系：开始 -->
      <button @click="fetchData">点我测试</button>
      <p v-if="backendMessage">
        <strong>后端消息:</strong> {{ backendMessage }}
      </p>
      <p v-if="errorMessage" style="color:red;">
        <strong>错误信息:</strong> {{ errorMessage }}
      </p>
      <!-- 测试下按钮和后端联系：结束 -->
    </div>
    <!-- 主显示区域 -->
    <div class="main-content" >
      <!-- 这里可以放置地图组件或其他内容 -->
      <h2>主显示区域</h2>
      <p>这里是主要内容区域，可以放置地图或其他组件。</p>
      <!-- 地图容器 -->
      <div id="mapid" style="height:100%;"></div>

    </div>

  </div>

</template>

<style scoped>
.app{
  display: flex;
  height: 100vh;
}
.sidebar{
  width: 320px; 
  background-color: #fff; 
  box-shadow:0 0 15px rgba(0,0,0,0.1); 
  position: fixed; /* 如果想要固定侧边栏 */
  padding:20px;
  z-index:1000;
  left: 0;
  top: 0;
  height: 100vh;
  overflow-y: auto; /* 内容过多时可滚动 */
  text-align: left;
}
.sidebar-buttons {
  display: flex;
  border: 1px solid #0959c2;
  border-radius: 10px;
  overflow: hidden;
}
.sidebar-button-point {
  flex: 1; 
  border: none; 
  padding: 10px; 
  border-right: 1px solid #0959c2; 
  border-radius: 10px 0 0 10px; 
  background-color: #ffffff;
  color: #0959c2;
}
.sidebar-button-rectangle {
  flex: 1; 
  border: none; 
  padding: 10px; 
  border-radius: 0 10px 10px 0; 
  background-color: #ffffff;
  color: #0959c2;
}
.basemap-select {
  width: 100%;
  height: 40px;
  font-size: 16px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
.main-content{
  flex: 1; 
  position: relative;
}
</style>
