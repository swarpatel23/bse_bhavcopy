<template>
  <div id="search-bar">
    <input
      v-model="search"
      @keyup="searchStock"
      type="text"
      id="name"
      placeholder="Search By Stock Name"
    />
  </div>
</template>
<script>
export default {
  name: "search-form",
  methods: {
    searchStock() {
      this.$emit("search:stock", this.search);
    },
  },
  computed: {},
  data() {
    return {
      search: "",
    };
  },
};
</script>

<style scoped></style>
