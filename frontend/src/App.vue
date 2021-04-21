<template>
  <div id="app" class="container">
    <h2 id="headline">
      BSE Latest Bhav Copy
    </h2>
    <h5>bhav copy available for date : {{ getDate() }}</h5>
    <div clas="small-container">
      <search-bar @search:stock="fetchStockData" />
      <download-excel :stocks="searchResult" />
      <view-stock :stocks="searchResult" />
    </div>
  </div>
</template>

<script>
import SearchBar from "./components/SearchBar.vue";
import ViewStock from "./components/ViewStock.vue";
import DownloadExcel from "./components/DownloadExcel.vue";
export default {
  name: "App",
  components: {
    SearchBar,
    ViewStock,
    DownloadExcel,
  },
  mounted() {},
  methods: {
    getDate() {
      const date = new Date();
      var present;
      if (date.getHours() < 18) {
        date.setDate(date.getDate() - 1);
      }
      var day = date.getDate();
      var month = date.getMonth() + 1;
      var year = date.getFullYear();
      present = day + " - " + month + " - " + year;
      return present;
    },
    async fetchStockData(search) {
      if (search != "") {
        console.log(`https://localhost:8000/api/?search=${search}`);
        try {
          const response = await fetch(
            `http://localhost:8000/api/?search=${search}`
          );
          this.searchResult = await response.json();
        } catch (error) {
          console.error(error);
        }
      } else {
        this.searchResult = {};
      }
    },
  },
  data() {
    return {
      searchResult: {},
      day: "",
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}

#headline {
  color: #2c3e50;
}
</style>
