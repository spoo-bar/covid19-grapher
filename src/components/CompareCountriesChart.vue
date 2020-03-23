<template>
  <div class="new-cases">
    <div class="row">
      <div class="col col-lg-3 col-sm-12">
        <div class="form-group">
          <br />
          <div class="custom-control custom-switch">
            <input
              type="checkbox"
              class="custom-control-input"
              id="useSevenDayAverage"
              v-model="useSevenDayAverage"
              v-bind:value="false"
              v-on:change="changeDataSource()"
            />
            <label class="custom-control-label" for="useSevenDayAverage">Use seven day average</label>
          </div>
          <br />
          <select name="country" id="country1" class="form-control" @change="changeCountry1">
            <option
              v-for="(country, index) in countries"
              :key="index"
              :value="country"
            >{{ country }}</option>
          </select>
          <br />
          <select name="country" id="country2" class="form-control" @change="changeCountry2">
            <option
              v-for="(country, index) in countries"
              :key="index"
              :value="country"
            >{{ country }}</option>
          </select>
        </div>
      </div>
      <div class="col col-lg-9 col-sm-12">
        <highcharts :options="chartOptions"></highcharts>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";
import Countries from "../assets/countries.json";
import NewCases from "../assets/new_cases.json";
import SmoothNewCases from "../assets/smooth_new_cases.json";

export default {
  name: "CompareCountriesChart",
  components: {
    highcharts: Chart
  },
  data() {
    return {
      chartOptions: {
        series: [
          {
            type: "spline",
            name: "World",
            data: [],
            color: "#6CC3D5",
            marker: {
              enabled: false
            }
          },
          {
            type: "spline",
            name: "World",
            data: [],
            color: "#F3969A",
            marker: {
              enabled: false
            }
          }
        ],
        title: {
          text: "Placeholder title"
        },
        tooltip: {
            useHTML: true,
            headerFormat: '<small>Day {point.key}</small><br/>'
        },
        xAxis: [
          {
            allowDecimals: false,
            labels: {
              formatter: function() {
                var label = this.axis.defaultLabelFormatter.call(this);
                return "Day " + label;
              }
            },
            title: {
              text: ""
            }
          }
        ],
        yAxis: [
          {
            allowDecimals: false,
            title: {
              text: "Number of cases"
            }
          }
        ]
      },
      countries: Countries,
      newCases: NewCases,
      smoothNewCases: SmoothNewCases,
      country1: "World",
      country2: "World",
      useSevenDayAverage: false
    };
  },
  methods: {
    changeCountry1: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      this.country1 = selectedCountry;
      this.chartOptions.title.text = this.country1 + " vs " + this.country2;
      this.chartOptions.series[0].data = this.getCovidData(selectedCountry);
      this.chartOptions.series[0].name = this.country1;
    },
    changeCountry2: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      this.country2 = selectedCountry;
      this.chartOptions.title.text = this.country1 + " vs " + this.country2;
      this.chartOptions.series[1].data = this.getCovidData(selectedCountry);
      this.chartOptions.series[1].name = this.country2;
    },
    changeDataSource: function() {
      this.chartOptions.series[0].data = this.getCovidData(this.country1);
      this.chartOptions.series[1].data = this.getCovidData(this.country2);
    },
    getCovidData: function(countryName) {
      if (this.useSevenDayAverage) {
        return this.smoothNewCases[countryName];
      } else {
        return this.newCases[countryName];
      }
    }
  },
  mounted: function() {
    this.chartOptions.title.text = "World vs World";
    this.chartOptions.series[0].data = this.newCases["World"];
    this.chartOptions.series[1].data = this.newCases["World"];
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
