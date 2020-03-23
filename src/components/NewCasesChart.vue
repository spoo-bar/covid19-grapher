<template>
  <div class="new-cases">
    <div class="row">
      <div class="col col-lg-3 col-sm-12">
        <div>
          <p class="card-text"><small>Seven day average is calculated to smoothen the day-to-day anomalies  </small></p>
          <br />
        </div>
        <div class="form-group">
          <select name="country" id="country" class="form-control" @change="changeCountry">
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

import {Chart} from 'highcharts-vue';
import Countries from "../assets/countries.json";
import NewCases from "../assets/new_cases.json";
import SmoothNewCases from "../assets/smooth_new_cases.json";

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
      smoothNewCases: SmoothNewCases
    };
  },
  methods: {
    changeCountry: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      this.chartOptions.title.text = selectedCountry;
      this.chartOptions.series[0].data = this.newCases[selectedCountry];
      this.chartOptions.series[1].data = this.smoothNewCases[selectedCountry];
    }
  },
  mounted: function() {
    this.chartOptions.title.text = "World";
    this.chartOptions.series[0].data = this.newCases["World"];
    this.chartOptions.series[1].data = this.smoothNewCases["World"];
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
