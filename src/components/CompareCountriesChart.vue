<template>
  <div class="new-cases">
    <div class="row">
      <div class="col-lg-3 col-sm-12">
        <div class="form-group">
          <br />
          <div class="custom-control custom-switch">
            <input
              type="checkbox"
              class="custom-control-input"
              id="useSevenDayAverage"
              v-model="useSevenDayAverage"
              v-bind:value="false"
              v-on:change="setSelectedCountryData()"
            />
            <label class="custom-control-label" for="useSevenDayAverage">Use seven day average</label>
          </div>
          <br />
          <select
            name="country"
            id="country1"
            class="form-control"
            v-model="selectedCountryOneName"
            @change="changeCountry1"
          >
            <option
              v-for="(country, index) in data.Data"
              :key="index"
              :value="country.Name"
            >{{ country.Name }}</option>
          </select>
          <br />
          <select name="country" id="country2" class="form-control" @change="changeCountry2">
            <option
              v-for="(country, index) in data.Data"
              :key="index"
              :value="country.Name"
            >{{ country.Name }}</option>
          </select>
        </div>
      </div>
      <div class="col-lg-9 col-sm-12">
        <highcharts :options="chartOptions"></highcharts>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";
import Data from "../assets/data.json";

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
          headerFormat: "<small>Day {point.key}</small><br/>"
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
      useSevenDayAverage: false,
      data: Data,
      selectedCountryOne: undefined,
      selectedCountryTwo: undefined,
      selectedCountryOneName: ""
    };
  },
  methods: {
    changeCountry1: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      this.selectedCountryOne = this.data.Data.filter(
        c => c.Name === selectedCountry
      )[0];
      this.setSelectedCountryData();
    },
    changeCountry2: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      this.selectedCountryTwo = this.data.Data.filter(
        c => c.Name === selectedCountry
      )[0];
      this.setSelectedCountryData();
    },
    getCovidData: function(country) {
      if (this.useSevenDayAverage) {
        return country.NewCases.SevenDayAvgSinceFirstCase;
      } else {
        return country.NewCases.DayCountSinceFirstCase;
      }
    },
    setSelectedCountryData: function() {
      this.chartOptions.title.text =
        this.selectedCountryOne.Name + " vs " + this.selectedCountryTwo.Name;
      this.chartOptions.series[0].name = this.selectedCountryOne.Name;
      this.chartOptions.series[0].data = this.getCovidData(
        this.selectedCountryOne
      );
      this.chartOptions.series[1].name = this.selectedCountryTwo.Name;
      this.chartOptions.series[1].data = this.getCovidData(
        this.selectedCountryTwo
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
    this.selectedCountryOneName = this.getDefaultCountry();
    this.selectedCountryOne = this.data.Data.filter(
      c => c.Name === this.selectedCountryOneName
    )[0];
    this.selectedCountryTwo = this.data.Data.filter(c => c.Name === "World")[0];
    this.setSelectedCountryData();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
