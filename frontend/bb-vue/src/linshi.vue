<template>
  <!-- 1. 外层容器 div，应用 CSS 类名 sidebar-buttons -->
  <div class="sidebar-buttons">
    
    <!-- 2. 第一个按钮：点选模式 -->
    <button 
      <!-- 3. 基础 CSS 类名，定义按钮的默认样式 -->
      class="sidebar-button"
      <!-- 4. 动态类绑定：当 selectedMode === 'point' 时添加 
       active 类 -->
      <!-- 关联 script：读取 data() 中的 selectedMode 变量进行比较 -->
      :class="{ active: selectedMode === 'point' }"
      <!-- 5. 点击事件：调用 selectMode 方法并传入参数 'point' -->
      <!-- 关联 script：触发 methods 中的 selectMode('point') 方法 -->
      @click="selectMode('point')"
    >
      点选模式 <!-- 6. 按钮显示的文本 -->
    </button>
    
    <!-- 7. 第二个按钮：框选模式 -->
    <button 
      <!-- 8. 基础 CSS 类名，与第一个按钮相同的默认样式 -->
      class="sidebar-button"
      <!-- 9. 动态类绑定：当 selectedMode === 'rectangle' 时添加 active 类 -->
      <!-- 关联 script：读取 data() 中的 selectedMode 变量进行比较 -->
      :class="{ active: selectedMode === 'rectangle' }"
      <!-- 10. 点击事件：调用 selectMode 方法并传入参数 'rectangle' -->
      <!-- 关联 script：触发 methods 中的 selectMode('rectangle') 方法 -->
      @click="selectMode('rectangle')"
    >
      框选模式 <!-- 11. 按钮显示的文本 -->
    </button>
  </div>
</template>

<script>
export default {
  // 12. 组件名称，用于 Vue DevTools 调试和组件注册
  name: 'SidebarButtons',
  
  // 13. data() 函数：定义组件的响应式数据
  data() {
    return {
      // 14. selectedMode：当前选中的模式，默认值为 'point'
      // 关联 template：被 :class 绑定读取，用于判断哪个按钮应该有 active 类
      selectedMode: 'point' 
    }
  },
  
  // 15. methods 对象：定义组件的方法
  methods: {
    // 16. selectMode 方法：处理按钮点击时的模式切换
    // 参数 mode：从 template 中的 @click 事件传入（'point' 或 'rectangle'）
    selectMode(mode) {
      // 17. 更新 selectedMode 的值
      // 关联 template：这会触发 :class 绑定重新计算，更新按钮样式
      this.selectedMode = mode;
      
      // 18. 向父组件发送自定义事件，传递当前选中的模式
      // 可选功能：让父组件知道模式已切换
      this.$emit('mode-changed', mode);
    }
  }
}
</script>

<style scoped>
/* 19. scoped：样式只作用于当前组件，不会影响其他组件 */

/* 20. 外层容器样式：关联 template 第1行的 class="sidebar-buttons" */
.sidebar-buttons {
  display: flex;        /* 21. 使用弹性布局 */
  gap: 8px;            /* 22. 按钮之间的间距 */
  margin-bottom: 16px; /* 23. 容器底部外边距 */
}

/* 24. 按钮默认样式：关联 template 中的 class="sidebar-button" */
.sidebar-button {
  flex: 1;                    /* 25. 按钮等宽分布 */
  padding: 8px 16px;          /* 26. 按钮内边距 */
  border: 2px solid #007bff;  /* 27. 蓝色边框 */
  border-radius: 4px;         /* 28. 圆角 */
  cursor: pointer;            /* 29. 鼠标悬停时显示手型 */
  font-size: 14px;           /* 30. 字体大小 */
  font-weight: 500;          /* 31. 字体粗细 */
  transition: all 0.2s ease; /* 32. 所有属性变化的过渡动画 */
  
  /* 33-34. 默认状态样式：白色背景 + 蓝色文字 */
  background-color: white;
  color: #007bff;
}

/* 35. 按钮悬停状态：关联所有 .sidebar-button 元素 */
.sidebar-button:hover {
  opacity: 0.8; /* 36. 悬停时透明度降低 */
}

/* 37. 按钮选中状态：关联 template 中的动态类绑定 :class="{ active: ... }" */
/* 当 selectedMode 匹配时，对应按钮会获得这个 active 类 */
.sidebar-button.active {
  /* 38-39. 选中状态样式：蓝色背景 + 白色文字（与默认状态相反） */
  background-color: #007bff;
  color: white;
}

/* 40. 响应式设计：屏幕宽度小于768px时 */
@media (max-width: 768px) {
  .sidebar-buttons {
    flex-direction: column; /* 41. 按钮垂直排列 */
  }
}
</style>
