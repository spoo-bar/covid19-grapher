<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <router-link to="/" class="navbar-brand">COVID19</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarDropdown"
        aria-controls="navbarDropdown"
        aria-expanded="true"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarDropdown">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
          <!-- <li class="nav-item">
            <a class="nav-link" href="https://forms.gle/HGUSUm8gnnWwaS3C8" target="_blank">Feedback</a>
          </li> -->
          <li class="nav-item">
            <a
              class="nav-link"
              target="_blank"
              href="https://ourworldindata.org/coronavirus-source-data"
            >Sources</a>
          </li>
        </ul>
      </div>
    </nav>

    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<style scoped>
button.navbar-toggler {
  border: none;
}
</style>
