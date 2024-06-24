<template>
  <div id="app">
    <h1>Natural language to Linear-time Temporal Logic</h1>
    <span>model: </span>
    <select v-model="selectedNumber" class="dropdown">
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.label }}
      </option>
    </select>
    <input v-model="inputData" placeholder="Enter some data">
    <button @click="submitData">Submit</button>
    <p>Processed Data: {{ processedData }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedValue: 1, // 用于接口调用的实际值
      options: [ // 下拉框的选项，模拟接口返回的值，包含显示的标签和实际的值
        {label: 'kimi', value: 1},
        {label: 'gpt4o', value: 2},
      ],
      inputData: '',
      processedData: ''
    };
  },
  methods: {
    async submitData() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/process', {inputData: this.inputData});
        this.processedData = response.data.processedData;
      } catch (error) {
        console.error('Error processing data:', error);
      }
    },
    handleSelection() {
      // 使用 this.selectedValue 作为调用接口的参数
      console.log("Selected value for API call:", this.selectedValue);
      // 这里添加调用接口的代码
    },
    // watch: {
    //   // 监听 selectedValue 的变化，以便在值改变时执行某些操作
    //   selectedValue(newValue) {
    //     this.handleSelection();
    //   }
    // }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
