import { defineStore } from 'pinia'

//defining a store
export const useLoggedInUserStore = defineStore({
  // id is only required for devtools with the Pinia store
  id: 'loggedInUser',
  //central part of the store
  state: () => {
    return {
      name: "",
      role: 0,
      isLoggedIn: false,
    }
  },
// Send username and password to the simulated loginAPI
// If the username and password match, set isAllowed to true and direct user to the home page using router otherwise an error message
actions: {
  async login(username, password) {
    try {
      const response = await apiLogin(username, password);
      this.$patch({
        isLoggedIn: response.isAllowed,
        role: response.role,
        name: response.name
      })
      if (response.isAllowed) {
        this.$router.push("/");
      } else {
        this.$store.commit("setUser", null);
        alert("Invalid credentials. Please try again.");
      }
    } catch (error) {
      console.log(error)
      alert("Invalid credentials. Please try again.");
    }
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
});
//login API to check username and password match
//username and password the same for now. Best to keep it simple for testing
function apiLogin(u, p) {
if (u === "admin" && p === "admin") {
  return Promise.resolve({ isAllowed: true, role: 1, name: "Admin" });
}
if (u === "viewer" && p === "viewer") {
  return Promise.resolve({ isAllowed: true, role: 2, name: "Viewer" });
}
return Promise.reject(new Error("invalid"));
}

//defining a store for findService.Vue
export const findServicesStore = defineStore({

id: 'findServicesStore',
state: () => {
  return {
    services: [
      {
        serviceID: 101,
        serviceName: 'Family Support',
        serviceDescription: 'Offering support to family members.',
        serviceStatus: 'active'
      },
      {
        serviceID: 102,
        serviceName: 'Adult Education',
        serviceDescription: 'Adult teaching session.',
        serviceStatus: 'active'
      },
      {
        serviceID: 103,
        serviceName: 'Youth Services Program',
        serviceDescription: 'Various activities dedicated to young people.',
        serviceStatus: 'active'
      },
      {
        serviceID: 104,
        serviceName: 'Childhood Education',
        serviceDescription: 'Children teaching session.',
        serviceStatus: 'active'
      }

    ]
  }
},


actions: {

}
});