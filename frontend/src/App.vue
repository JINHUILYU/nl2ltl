<template>
  <div id="app">
    <h1>Natural language to Linear-time Temporal Logic</h1>
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
      inputData: '',
      processedData: ''
    };
  },
  methods: {
    async submitData() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/process', { inputData: this.inputData });
        this.processedData = response.data.processedData;
      } catch (error) {
        console.error('Error processing data:', error);
      }
    }
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
