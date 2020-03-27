<template>
  <div class="last-update-time">
    <p class="text-right"><small>Data last updated at {{ data.LastUpdateTime | toLocaleDateString }} {{ data.LastUpdateTime | toLocaleTimeString }}</small></p>
  </div>
</template>

<script>
import Data from "../assets/data.json";

export default {
  name: "LastUpdateTime",
  data() {
    return {
      data: Data
    };
  },
  filters: {
    toLocaleDateString(date) {
      return new Date(date).toLocaleDateString();
    },
    toLocaleTimeString(date) {
      return new Date(date).toLocaleTimeString();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
