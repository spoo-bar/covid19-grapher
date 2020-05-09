<template>
  <div class="death-rate-table">
    <div class="row justify-content-around">
      <table v-if="displayData.length > 0" class="table col-lg-12">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">Death Rate</th>
            <th scope="col">Name</th>
            <th scope="col">Total Cases</th>
            <th scope="col">Deaths</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="country in displayData" :key="country.name">
            <th scope="row">#{{ country.rank }}</th>
            <td>{{ country.deathRate }}%</td>
            <td>
              {{ country.name }}
              <span
                class="badge badge-pill badge-secondary"
                v-show="country.name === defaultCountry && country.name !== 'World'"
              >Default</span>
              <span v-show="country.name ==='World'">🌏</span>
            </td>
            <td>{{ country.totalConfirmedCases | toLocaleNumberString }}</td>
            <td>{{ country.totalDeathCount | toLocaleNumberString }}</td>
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
  filters: {
    toLocaleNumberString(number) {
      let locale = navigator.language;
      return new Number(number).toLocaleString(locale);
    }
  },
  data() {
    return {
      data: Data,
      displayData: [],
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
    loadData() {
      let tableData = [];
      this.displayData = [];

      let highestConfirmedCases = this.getHighestConfirmedCases();
      for (let country of this.data.Data) {
        let deathRate = this.getDeathRate(country);
        if (deathRate > 0 && country.TotalCasesCount > highestConfirmedCases) {
          let countryData = {
            name: country.Name,
            deathRate: deathRate
          };
          tableData.push(countryData);
        }
      }
      tableData.sort(
        (a, b) => parseFloat(b.deathRate) - parseFloat(a.deathRate)
      );

      for (let i = 1; i <= 10; i++) {
        let country = this.getCountryData(tableData[i - 1].name);
        this.displayData.push({
          rank: i,
          name: tableData[i - 1].name,
          deathRate: tableData[i - 1].deathRate,
          totalConfirmedCases: country.TotalCasesCount,
          totalDeathCount: country.TotalDeathsCount
        });
      }
    },
    getHighestConfirmedCases: function() {
      let totalCasesList = this.data.Data.map(c => c.TotalCasesCount);
      totalCasesList.sort((a, b) => b - a);
      totalCasesList = totalCasesList.slice(0, 11);
      totalCasesList.reverse();
      // returning the 10th highest value
      return parseInt(totalCasesList[0]);
    },
    getCountryData: function(selectedCountry) {
      return this.data.Data.filter(c => c.Name === selectedCountry)[0];
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
    this.defaultCountry = this.getDefaultCountry();
    this.loadData();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
