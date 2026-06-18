<template>

  <div>

    <nav class="navbar">

      <div class="title">
        Workload Platform
      </div>

      <div class="menu">

        <router-link to="/">
          Dashboard
        </router-link>

        <router-link to="/workloads">
          Workloads
        </router-link>

        <router-link to="/history">
          History
        </router-link>

        <router-link to="/compare">
          Compare
        </router-link>

        <router-link to="/report">
          Report
        </router-link>

      </div>

    </nav>

    <router-view />

  </div>

</template>

<style scoped>

.navbar {
    background: #003c71;
    color: white;
    padding: 15px 30px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.title {
    font-size: 22px;
    font-weight: bold;
}

.menu a {
    color: white;
    text-decoration: none;
    margin-left: 25px;
}

.menu a:hover {
    color: #8ec5ff;
}

</style>