<template>
  <div class="home">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Has the country flattened the curve?</h4>
        <NewCasesChart />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NewCasesChart from "@/components/NewCasesChart.vue";

export default {
  name: "Home",
  components: {
    NewCasesChart
  }
};
</script>

<style>
.home {
  margin-top: 2rem;
}
</style>
