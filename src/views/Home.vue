<template>
  <div class="home">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Has the country flattened the curve?</h4>
        <NewCasesChart />
      </div>
    </div>
    <br />
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Compare countries</h4>
        <h6 class="card-subtitle mb-2 text-muted">Compare the rise of new cases between two countries</h6>
        <CompareCountriesChart />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NewCasesChart from "@/components/NewCasesChart.vue";
import CompareCountriesChart from "@/components/CompareCountriesChart.vue";

export default {
  name: "Home",
  components: {
    NewCasesChart,
    CompareCountriesChart
  }
};
</script>

<style>
.home {
  margin-top: 2rem;
}
</style>
