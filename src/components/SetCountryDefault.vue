<template>
  <div class="new-cases">
    <div class="form-group">
      <select name="country" id="country" class="form-control" v-model="selectedCountry" @change="changeCountry">
        <option
          v-for="(country, index) in data.Data"
          :key="index"
          :value="country.Name"
        >{{ country.Name }}</option>
      </select>
    </div>
  </div>
</template>

<script>
import Data from "../assets/data.json";

export default {
  name: "SetCountryDefault",
  components: {},
  data() {
    return {
      data: Data,
      selectedCountry: undefined,
    };
  },
  methods: {
    changeCountry: function(e) {
      let selectedCountry = e.target.options[event.target.selectedIndex].text;
      localStorage.setItem('defaultCountry', selectedCountry);
      location.reload();
    },
    getDefaultCountry: function() {
      let defaultCountry = localStorage.getItem('defaultCountry');
      if (defaultCountry) {
        return defaultCountry;
      }
      else {
        return "World";
      }
    }
  },
  mounted: function() {
    this.selectedCountry = this.data.Data.filter(c => c.Name === this.getDefaultCountry())[0];
    this.selectedCountry = this.selectedCountry.Name;
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
</style>
