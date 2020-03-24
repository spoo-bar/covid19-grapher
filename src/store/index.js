import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    defaultCountry: "World"
  },
  getters: {
    getDefaultCountry: state => {
      let setCountry = localStorage.getItem('defaultCountry');
      if (setCountry) {
        return setCountry;
      }
      else {
        return state.defaultCountry;
      }
    }
  },
  mutations: {
    setDefaultCountry(state, payload) {
      state.defaultCountry = payload;
      localStorage.setItem('defaultCountry', payload);
    }
  },
  actions: {
  },
  modules: {
  }
})
