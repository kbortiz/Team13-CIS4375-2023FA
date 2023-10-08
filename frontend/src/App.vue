<!-- Display only a portion in the navigation panel until someone logs in-->

<template>
  <main class="flex flex-row">
    <div id="_container" class="h-screen">
      <header class="w-full">
        <section class="text-center">
          <img class="m-auto" src="@\assets\DanPersona.svg" />
        </section>
        <nav class="mt-10">
          <ul class="flex flex-col gap-4">
              <li class="nav-item" v-if="!user.isLoggedIn">
              <router-link to="/login">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >login</span
                >
                Login
              </router-link>
              </li>
              <li v-if="user.isLoggedIn">
                <a>                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >account_circle</span
                > Welcome, {{ user.name }}
              </a>
            </li>
            <li v-if = "user.isLoggedIn">
              <router-link to="/">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >dashboard</span
                >
                Dashboard
              </router-link>
            </li>
            <li v-if="user.isLoggedIn && user.role === 1">
              <router-link to="/intakeform">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >people</span
                >
                Add Customer
              </router-link>
            </li>
            <li v-if="user.isLoggedIn && user.role === 1">
              <router-link to="/findclient">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >person_search</span
                >
                Customer List
              </router-link>
            </li>
            <li v-if="user.isLoggedIn && user.role === 1">
              <router-link to="/eventform">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >event</span
                >
                Create Promotion
              </router-link>
            </li>
            <li v-if="user.isLoggedIn && user.role === 1">
              <router-link to="/findevents">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >search</span
                >
                Promotion List
              </router-link>
            </li>
            <li v-if="user.isLoggedIn && user.role === 2">
              <router-link to="/addservice">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >add_circle</span>
                Check-in & Review
              </router-link>
            </li>
            <li v-if="user.isLoggedIn  && user.role === 1">
              <router-link to="/findservice">
                <span
                  style="position: relative; top: 6px"
                  class="material-icons"
                  >manage_search</span
                >
                Manage Review
              </router-link>
            </li>
            
            <li v-if="user.isLoggedIn">
                <br>
                <a href="">
                  <span
                  @click="store.logout()" class="nav-link"><i style="position: relative; top: 6px"
                  class="material-icons">logout</i>
                  </span> Logout 
                </a>
              </li>
            
          </ul>
        </nav>
      </header>
    </div>
    <div class="grow w-4/5">
      <section
        class="justify-end items-center h-24 flex"
        style="background: linear-gradient(250deg, #c8102e 70%, #efecec 50.6%)"
      >
        <h1 class="mr-20 text-3xl text-white">{{ this.orgName }}</h1>
      </section>
      <div>
        <router-view></router-view>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios'
const apiURL = import.meta.env.VITE_ROOT_API
import { useLoggedInUserStore } from "@/store/loggedInUser";

export default {
  name: 'App',
  data() {
    return {
      orgName: 'Dataplatform'
    }
  },
  created() {
    axios.get(`${apiURL}/org`).then((res) => {
      this.orgName = res.data.name
    })
  },
    setup() {
    const user = useLoggedInUserStore();
    return { user };
  },


logout() {
    //Reset value after user log out
    this.patch({
      name: "",
      role: 0,
      isLoggedIn: false,
    });
    this.$router.push("/login");
  }
}

</script>


<style>
#_container {
  background-color: #c8102e;
  color: white;
  padding: 18px;
}
</style>
