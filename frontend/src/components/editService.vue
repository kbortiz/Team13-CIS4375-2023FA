<script>
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import axios from 'axios';
const apiURL = import.meta.env.VITE_ROOT_API
export default {
  name: 'serviceform',
  setup() {
    return { v$: useVuelidate({ $autoDirty: true }) }
  },  
  data()
  {
    return{
      services: JSON.parse(localStorage.getItem('service')) || [],
      selectedData: {},
      updateService: [],
      error: ''
    }
  },
  created() {
    //In this created hook, find the service in the local storage that has the service id matching the id in the URL
    const serviceid = this.$route.params.id // get the ID from the URL
    const storedData = JSON.parse(localStorage.getItem('service')) // pull all the value matching the service key in the local storage
    const selecteddata = storedData.find((item) => item.id == serviceid) // find the service that has the service id matching the id in the URL
    if (selecteddata) {
      this.selectedData = selecteddata // store the service detail in the selectedData object and display in the form
    }
  },
   methods: {    
    async handleSubmitForm() {
      this.error = '';
      // Check if the service name field in the form is filled, if not, prompt an error message
      if (!this.selectedData.name)
      {
        this.error = 'Service Name is required'
      }
      // If no errors found. then the form is submitted
      if (this.error==='') 
      {
        /* axios
          .post(`${apiURL}/services`, this.service)
          .then(() => {
            alert('Event has been added.')
            this.$router.push({ name: 'findservice' })
          })
          .catch((error) => {
            console.log(error)
          }) */
      // Retrieve the service details from the local storage and store in the services
      // Update one of the object in the services using map function and store the new services object in updateService
      // Push the new updateService to the local storage, prompt a successful message and direct to addService view using router
        this.updateService = this.services.map((s) => {
          if (s.id == this.selectedData.id) {
              return { ...s, ...this.selectedData};
            }
            else
            { return s;}
          });
          localStorage.setItem('service', JSON.stringify(this.updateService));
          alert('Service information updated successfully!');
          this.$router.push({name:'addService'});
      }
    },
  }, 
};

</script>
<template>
  <main>
    <div>
      <h1
        class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10"
      >
        Edit Service
      </h1>
    </div>
    <div class="px-10 py-20">
      <!-- @submit.prevent stops the submit event from reloading the page-->
      <form id="serviceForm" @submit.prevent="handleSubmitForm">
        <!-- grid container -->
        <div
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10"
        >
          <h2 class="text-2xl font-bold">Service Details</h2>
          <!-- form field -->
          <div class="flex flex-col">
            <label class="block">
              <span class="text-gray-700">Service Name</span>
              <span style="color: #ff0000">*</span>
              <input
                type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="selectedData.name"
              /> 
              <span class="text-black" v-if="error">
                <p class="text-red-700" >
                  {{ error }}!
                </p>
              </span>
            </label>
          </div>    
          <div></div>
          <div></div>
          <div></div>
          <!-- form field -->
          <div class="flex flex-col">
            <label class="block">
              <span class="text-gray-700">Description</span>
              <textarea
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                rows="2" v-model="selectedData.desc"></textarea>
            </label>
          </div>
          <div></div>
          <div></div>
          <!-- form field -->
          <div><h2 class="text-2xl font-bold">Service Status</h2></div>
            <div>
              <label for="active" class="inline-flex items-center">
                <input
                  type="radio"
                  id="Active"
                  value="Active"
                  v-model="selectedData.status"
                  class=" border-gray-300 text-indigo-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-offset-0 focus:ring-indigo-200 focus:ring-opacity-50"
                  
                />
                <span class="ml-3">Active</span>
              </label>
              <label for="inactive" class="inline-flex items-center">
                <input
                  type="radio"
                  id="Inactive"
                  value="Inactive"
                  v-model="selectedData.status"
                  class=" border-gray-300 text-indigo-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-offset-0 focus:ring-indigo-200 focus:ring-opacity-50"
                  
                />
                <span class="ml-3">Inactive</span>
              </label>
            </div>
       <div class="flex justify-between mt-10 mr-20">
          <button class="bg-red-700 text-white rounded">
              Edit Service
          </button>
        </div>
        </div>
      </form>
    </div>
  </main>
</template>
