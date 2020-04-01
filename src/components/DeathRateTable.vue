<template>
  <div class="death-rate-table">
    <div class="row">
      <table v-if="displayData1.length > 0" class="table col-lg-6">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">Death Rate</th>
            <th scope="col">Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="country in displayData1" :key="country.name">
            <th scope="row">#{{ country.rank }}</th>
            <td>{{ country.deathRate }}%</td>
            <td>
              {{ country.name }}
              <span
                class="badge badge-pill badge-secondary"
                v-show="country.name === defaultCountry"
              >Default</span>
            </td>
          </tr>
        </tbody>
      </table>
      <table v-if="displayData2.length" class="table col-lg-6">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">Death Rate</th>
            <th scope="col">Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="country in displayData2" :key="country.name">
            <th scope="row">#{{ country.rank }}</th>
            <td>{{ country.deathRate }}%</td>
            <td>
              {{ country.name }}
              <span
                class="badge badge-pill badge-secondary"
                v-show="country.name === defaultCountry"
              >Default</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
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
      displayData1: [],
      displayData2: [],
      defaultCountry: ""
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
    },
    getDefaultCountry: function() {
      let defaultCountry = localStorage.getItem("defaultCountry");
      if (defaultCountry) {
        return defaultCountry;
      } else {
        return "World";
      }
    }
  },
  mounted: function() {
    this.loadData();
    for (let i = 1; i <= 10; i++) {
      this.displayData1.push({
        rank: i,
        name: this.tableData[i-1].name,
        deathRate: this.tableData[i-1].deathRate,
        confirmedCases: this.getCountryData(this.tableData[i-1].name)
          .TotalCasesCount,
        deathCases: this.getCountryData(this.tableData[i-1].name).TotalDeathsCount
      });
    }
    for (let i = 11; i <= 20; i++) {
      this.displayData2.push({
        rank: i,
        name: this.tableData[i-1].name,
        deathRate: this.tableData[i-1].deathRate,
        confirmedCases: this.getCountryData(this.tableData[i-1].name)
          .TotalCasesCount,
        deathCases: this.getCountryData(this.tableData[i-1].name).TotalDeathsCount
      });
    }
    this.defaultCountry = this.getDefaultCountry();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
