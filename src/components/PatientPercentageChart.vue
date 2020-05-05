<template>
  <div class="patient-percentage-chart">
    <highcharts :options="chartOptions"></highcharts>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";
import Data from "../assets/data.json";

export default {
  name: "PatientPercentageChart",
  components: {
    highcharts: Chart
  },
  data() {
    return {
      chartOptions: {
        accessibility: {
          point: {
            valueSuffix: "%"
          }
        },
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false,
          type: "pie"
        },
        credits: {
          enabled: false
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            colors: this.getPieColors(),
            cursor: "pointer",
            dataLabels: {
              enabled: true,
              format: "{point.name}: {point.percentage:.1f} %"
            }
          }
        },
        series: [
          {
            name: "Confirmed Cases",
            colorByPoint: true,
            data: []
          }
        ],
        title: {
          text: ""
        },
        tooltip: {
          pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>"
        }
      },
      data: Data
    };
  },
  methods: {
    getCountryData: function(countryName) {
      return this.data.Data.filter(c => c.Name === countryName)[0];
    },
    getPieColors: function() {
      let colors = [];
      colors.push("#6CC3D5");
      colors.push("#5BD4D3");
      colors.push("#66E3C3");
      colors.push("#8BEEA8");
      colors.push("#BFF68A");
      colors.push("#F9F871");
      colors.push("#9BDE7E");
      colors.push("#4BBC8E");
      colors.push("#039590");
      colors.push("#1C6E7D");
      return colors;
    },
  },
  mounted: function() {
    let worldTotalCases = this.getCountryData("World").TotalCases;
    let chartData = [];
    for (let country of this.data.Data) {
      if (country.Name !== "World") {
        let countryCases = country.TotalCases;
        let countryPercentage = (countryCases / worldTotalCases) * 100;
        let countryData = {
          name: country.Name,
          y: countryPercentage
        };
        chartData.push(countryData);
      }
    }
    chartData.sort((a, b) => b.y - a.y);

    let top14 = chartData.slice(0, 15);
    let lastFew = chartData.slice(15, chartData.length);

    let othersSum = 0.0;
    for (let lastCountries of lastFew) {
      othersSum += lastCountries.y;
    }

    top14.push({
      name: "Others",
      y: othersSum
    });
    this.chartOptions.series[0].data = top14;
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
