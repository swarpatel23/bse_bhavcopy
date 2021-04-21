<template>
  <div class="flex-row">
    <p class="flex-small"><small>* daily update at 6 PM IST.</small></p>
    <div class="flex-small text-right" id="download-button">
      <button type="button" class="accent-button" v-on:click="downloadExcel">
        Download Excel
      </button>
    </div>
  </div>
</template>

<script>
import XLSX from "xlsx";

export default {
  name: "download-excel",
  props: {
    stocks: Object,
  },
  methods: {
    downloadExcel() {
      var stock_list = [];
      var stock = {};
      for (const [stock_name, stock_value] of Object.entries(this.stocks)) {
        stock = {};
        stock["name"] = stock_name;
        for (const [key, value] of Object.entries(stock_value)) {
          stock[key] = value;
        }
        stock_list.push(stock);
      }
      console.log(stock_list);
      const data = XLSX.utils.json_to_sheet(stock_list);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, data, "data");
      XLSX.writeFile(wb, "demo.xlsx");
    },
  },
};
</script>

<style scoped></style>
