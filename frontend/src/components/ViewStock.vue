<template>
  <div id="stock-table">
    <table>
      <thead>
        <tr>
          <th>Stock Code</th>
          <th>Stock Name</th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(stock, stock_name) in stocks" :key="stock['code']">
          <td>{{ stock["code"] }}</td>
          <td>{{ stock_name }}</td>
          <td>{{ stock["open"] }}</td>
          <td>{{ stock["high"] }}</td>
          <td>{{ stock["low"] }}</td>
          <td>{{ stock["close"] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "view-stock",
  props: {
    stocks: Object,
  },
};
</script>

<style scoped></style>
