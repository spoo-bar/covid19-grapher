<template>
  <div class="new-cases">
    <div class="row">
      <div class="col-lg-3 col-sm-12">
        <h6 class="card-subtitle mb-2 text-muted">Select a country</h6>
        <div class="form-group">
          <select
            name="country"
            id="country"
            class="form-control"
            v-model="selectedCountryName"
            @change="changeCountry"
          >
            <option
              v-for="(country, index) in data.Data"
              :key="index"
              :value="country.Name"
            >{{ country.Name }}</option>
          </select>
        </div>
        <div>
          <p class="card-text">
            <small v-if="this.selectedCountry !== undefined">First case : {{ this.selectedCountry.FirstCaseDate | toLocaleDateString }}</small>
          </p>
          <br />
        </div>
      </div>
      <div class="col-lg-3 col-sm-12">
        <h6 class="card-subtitle mb-2 text-muted">Confirmed Cases</h6>
        <h2 class="text-info" v-if="this.selectedCountry !== undefined">{{ this.selectedCountry.TotalCases | toLocaleNumberString }}</h2>
        <highcharts :options="confirmedChartOptions"></highcharts>
      </div>
      <div class="col-lg-3 col-sm-12">
        <h6 class="card-subtitle mb-2 text-muted">Deaths</h6>
        <h2 class="text-warning" v-if="this.selectedCountry !== undefined">{{ this.selectedCountry.TotalDeaths | toLocaleNumberString }}</h2>
        <highcharts :options="deathChartOptions"></highcharts>
      </div>
      <div class="col-lg-3 col-sm-12">
        <h6 class="card-subtitle mb-2 text-muted">Death Rate</h6>
        <h2 class="text-danger" v-if="this.selectedCountry !== undefined">{{ this.selectedCountry | getDeathRate }}<small>%</small></h2>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";
import Data from "../assets/data.json";

export default {
  name: "QuickCountry",
  components: {
    highcharts: Chart
  },
  data() {
    return {
      confirmedChartOptions: {
        chart: {
          height: "20%",
          spacing: [0, 0, 0, 0]
        },
        credits: {
          enabled: false
        },
        series: [
          {
            type: "spline",
            name: "Seven day average",
            data: [],
            color: "#aaa",
            marker: {
              enabled: false
            },
            showInLegend: false,
            states: {
              hover: {
                enabled: false
              }
            }
          }
        ],
        title: {
          text: ""
        },
        tooltip: {
          enabled: false
        },
        xAxis: [
          {
            visible: false
          }
        ],
        yAxis: [
          {
            visible: false
          }
        ]
      },
      deathChartOptions: {
        chart: {
          height: "20%",
          spacing: [0, 0, 0, 0]
        },
        credits: {
          enabled: false
        },
        series: [
          {
            type: "spline",
            name: "Seven day average",
            data: [],
            color: "#aaa",
            marker: {
              enabled: false
            },
            showInLegend: false,
            states: {
              hover: {
                enabled: false
              }
            }
          }
        ],
        title: {
          text: ""
        },
        tooltip: {
          enabled: false
        },
        xAxis: [
          {
            visible: false
          }
        ],
        yAxis: [
          {
            visible: false
          }
        ]
      },
      data: Data,
      selectedCountry: undefined,
      selectedCountryName: ''
    };
  },
  filters: {
    toLocaleNumberString(number) {
      let locale = navigator.language;
      return new Number(number).toLocaleString(locale);
    },
    toLocaleDateString(date) {
      return new Date(date).toLocaleDateString();
    },
    getDeathRate(selectedCountry) {
      let totalDeaths = selectedCountry.TotalDeaths;
      let totalConfirmedCases = selectedCountry.TotalCases;
      let deathRate = totalDeaths/totalConfirmedCases*100;
      return (Math.round(deathRate * 100) / 100).toFixed(2);
    }
  },
  methods: {
    changeCountry: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      this.selectedCountry = this.data.Data.filter(
        c => c.Name === selectedCountry
      )[0];
      this.setSelectedCountryData();
    },
    setSelectedCountryData: function() {
      this.confirmedChartOptions.series[0].data = this.selectedCountry.Cases.TotalCountSinceFirst;
      this.deathChartOptions.series[0].data = this.selectedCountry.Deaths.DayCountSinceFirst;
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
    this.selectedCountryName = this.getDefaultCountry();
    this.selectedCountry = this.data.Data.filter(
      c => c.Name === this.selectedCountryName
    )[0];
    this.setSelectedCountryData();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  margin-bottom: -0.35rem;
}

span.fav a {
  text-decoration: none;
}

div.row div {
  margin-bottom: 0.25rem;
}
</style>
