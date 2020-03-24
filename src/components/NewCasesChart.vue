<template>
  <div class="new-cases">
    <div class="row">
      <div class="col col-lg-3 col-sm-12">
        <div>
          <p class="card-text">
            <small>Seven day average is calculated to smoothen the day-to-day anomalies</small>
          </p>
          <br />
        </div>
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
      </div>
      <div class="col col-lg-9 col-sm-12">
        <highcharts :options="chartOptions"></highcharts>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";
import Data from "../assets/data.json";

export default {
  name: "NewCasesChart",
  components: {
    highcharts: Chart
  },
  data() {
    return {
      chartOptions: {
        series: [
          {
            type: "column",
            name: "New cases",
            data: [],
            color: "#6CC3D5",
            opacity: 0.4
          },
          {
            type: "spline",
            name: "Seven day average",
            data: [],
            color: "#6CC3D5",
            marker: {
              enabled: false
            }
          }
        ],
        title: {
          text: "Placeholder title"
        },
        tooltip: {
          shared: true,
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
      data: Data,
      selectedCountry: undefined,
      selectedCountryName: ''
    };
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
      this.chartOptions.title.text = this.selectedCountry.Name;
      this.chartOptions.series[0].data = this.selectedCountry.NewCases.DayCountSinceFirstCase;
      this.chartOptions.series[1].data = this.selectedCountry.NewCases.SevenDayAvgSinceFirstCase;
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
</style>
