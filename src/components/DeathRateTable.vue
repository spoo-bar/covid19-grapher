<template>
  <div class="death-rate-table">
    <br />
    <div class="form-group">
      <div class="custom-control custom-switch">
        <input
          type="checkbox"
          class="custom-control-input"
          id="sort-order"
          v-model="sortDecreasing"
          v-on:change="onSortOrderChange()"
        />
        <label class="custom-control-label" for="sort-order">Sort in decreasing order</label>
      </div>
    </div>
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
      displayData1: [],
      displayData2: [],
      defaultCountry: "",
      sortDecreasing: true
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
      this.displayData1 = [];
      this.displayData2 = [];

      for (let country of this.data.Data) {
        let deathRate = this.getDeathRate(country);
        if (deathRate > 0) {
          let countryData = {
            name: country.Name,
            deathRate: deathRate
          };
          tableData.push(countryData);
        }
      }

      if (this.sortDecreasing) {
        tableData.sort(
          (a, b) => parseFloat(b.deathRate) - parseFloat(a.deathRate)
        );
      } else {
        tableData.sort(
          (a, b) => parseFloat(a.deathRate) - parseFloat(b.deathRate)
        );
      }

      for (let i = 1; i <= 10; i++) {
        this.displayData1.push({
          rank: i,
          name: tableData[i - 1].name,
          deathRate: tableData[i - 1].deathRate
        });
      }
      for (let i = 11; i <= 20; i++) {
        this.displayData2.push({
          rank: i,
          name: tableData[i - 1].name,
          deathRate: tableData[i - 1].deathRate
        });
      }
    },
    onSortOrderChange: function() {
      this.loadData();
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
    this.defaultCountry = this.getDefaultCountry();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
