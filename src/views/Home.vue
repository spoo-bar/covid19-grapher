<template>
  <div class="home">
    <LastUpdateTime />
    <div class="row">
      <div class="col-lg-10">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Quick info</h4>
            <QuickCountry />
          </div>
        </div>
      </div>
      <div class="col-lg-2">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Default</h5>
            <SetCountryDefault />
            <p class="card-text">
              <small>Set a country as default and automatically load the country's data</small>
            </p>
          </div>
        </div>
      </div>
      <!-- <div class="d-none d-lg-block col-lg-2">
        <div class="card">
          <div class="card-body download-card">
            <h5 class="card-title">Download</h5>
            <a href="/data.json" download="data.json" target="_blank">
              <img
                src="data:image/png;base64,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"
                width="50"
              />
            </a>
            <p class="card-text">
              <small>
                Download the data used for these visualizations as JSON.
                <a
                  href="/schema.json"
                  download="schema.json"
                  target="_blank"
                >[Schema]</a>
              </small>
            </p>
          </div>
        </div>
      </div>-->
    </div>
    <br />
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Has the country flattened the curve?</h4>
        <NewCasesChart />
      </div>
    </div>
    <br />
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Compare countries</h4>
        <h6
          class="card-subtitle mb-2 text-muted"
        >Compare the rise of new cases between two countries</h6>
        <CompareCountriesChart />
      </div>
    </div>
    <br />
    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Death Rate Ranking</h4>
            <h6
              class="card-subtitle mb-2 text-muted"
            >Countries ranked by death rates</h6>
            <p class="card-text">
              <small>The top ten countries with highest number of confirmed cases are considered.</small>
            </p>
            <DeathRateTable />
          </div>
        </div>
      </div>
    </div>
    <br />
    <div class="alert alert-dismissible alert-warning">
      <button type="button" class="close" data-dismiss="alert">&times;</button>
      <strong>This project is at its end-of-life</strong> The visualization data will be automatically updated daily. 
      However, there will be no new features or bug fixes. In case you need to contact me, <a href="mailto:s.spoorti@gmail.com" class="alert-link"> click here</a>
    </div>
    <br />
    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Patient Percentage</h4>
            <h6
              class="card-subtitle mb-2 text-muted"
            >Percentage representation of confirmed cases by country</h6>
            <PatientPercentageChart />
          </div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Dead Patients Percentage</h4>
            <h6
              class="card-subtitle mb-2 text-muted"
            >Percentage representation of dead patients cases by country</h6>
            <DeadPatientPercentageChart />
          </div>
        </div>
      </div>
    </div>
    <br />
    
  </div>
</template>

<script>
// @ is an alias to /src
import NewCasesChart from "@/components/NewCasesChart.vue";
import CompareCountriesChart from "@/components/CompareCountriesChart.vue";
import QuickCountry from "@/components/QuickCountry.vue";
import SetCountryDefault from "@/components/SetCountryDefault.vue";
import LastUpdateTime from "@/components/LastUpdateTime.vue";
import PatientPercentageChart from "@/components/PatientPercentageChart.vue";
import DeadPatientPercentageChart from "@/components/DeadPatientPercentageChart.vue";
import DeathRateTable from "@/components/DeathRateTable.vue";

export default {
  name: "Home",
  components: {
    NewCasesChart,
    CompareCountriesChart,
    QuickCountry,
    SetCountryDefault,
    LastUpdateTime,
    PatientPercentageChart,
    DeadPatientPercentageChart,
    DeathRateTable
  }
};
</script>

<style>
.home {
  margin-top: 2rem;
}

.download-card {
  text-align: center;
}

.download-card img {
  padding: 5px;
}

.download-card p small {
  text-align: justify;
}
</style>
