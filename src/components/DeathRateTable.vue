<template>
  <div class="death-rate-table">
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">Name</th>
          <th scope="col">Death Rate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="country in displayData" :key="country.name">
          <th scope="row">#{{ country.rank }}</th>
          <td>{{ country.name }}</td>
          <td>{{ country.deathRate }}%</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Data from "../assets/data.json";

export default {
  name: "DeathRateTable",
  data() {
    return {
      data: Data,
      tableData: [],
      displayData: []
    };
  },
  methods: {
    getDeathRate(selectedCountry) {
      let totalDeaths = selectedCountry.TotalDeathsCount;
      let totalConfirmedCases = selectedCountry.TotalCasesCount;
      let deathRate = (totalDeaths / totalConfirmedCases) * 100;
      return (Math.round(deathRate * 100) / 100).toFixed(2);
    },
    getCountryData(selectedCountry) {
      return this.data.Data.filter(c => c.Name === selectedCountry)[0];
    },
    loadData() {
      for (let country of this.data.Data) {
        let deathRate = this.getDeathRate(country);
        let countryData = {
          name: country.Name,
          deathRate: deathRate
        };
        this.tableData.push(countryData);
      }

      this.tableData.sort(
        (a, b) => parseFloat(b.deathRate) - parseFloat(a.deathRate)
      );
    }
  },
  mounted: function() {

      this.loadData();
    for (let i = 1; i <= 10; i++) {
      this.displayData.push({
        rank: i,
        name: this.tableData[i].name,
        deathRate: this.tableData[i].deathRate,
        confirmedCases: this.getCountryData(this.tableData[i].name)
          .TotalCasesCount,
        deathCases: this.getCountryData(this.tableData[i].name).TotalDeathsCount
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
