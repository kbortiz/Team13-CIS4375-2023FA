<script>
import { DateTime } from 'luxon'
import axios from 'axios'
const apiURL = import.meta.env.VITE_ROOT_API

export default {
  data() {
    return {
      services: [],
      // Parameter for search to occur
      searchBy: '',
      serviceName: '',
      serviceDescription: '',
    }
  },
  mounted() {
    this.getServices()
  },
  methods: {
    handleSubmitForm() {
      let endpoint = ''
      if (this.searchBy === 'Service Name') {
        endpoint = `services/search/?serviceName="${this.serviceName}"&searchBy=name`
      } else if (this.searchBy === 'Service Description') {
        endpoint = `services/search/?serviceDescription"${this.serviceDescription}"&searchBy=description`
      }
      axios.get(`${apiURL}/${endpoint}`).then((res) => {
        this.services = res.data
      })
     },
    // abstracted method to get services
    getServices() {
      axios.get(`${apiURL}/services`).then((res) => {
        this.services = res.data
      })
      window.scrollTo(0, 0)
    },
    clearSearch() {
      // Resets all the variables
      this.searchBy = 'Service Name'
      this.serviceName = ''
      this.serviceDescription = ''
      
      this.getServices()
    },
    editService(serviceID) {
      this.$router.push({ name: 'editservice', params: { id: serviceID } })
    }
  }
}
</script>
<template>
  <main>
    <div>
      <h1
        class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10"
      >
        List of Reviews (WIP)
      </h1>
    </div>
    <div class="px-10 pt-20">
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10"
      >
        <h2 class="text-2xl font-bold">Review Search</h2>
        <!-- Displays Service Name search field -->
        <div class="flex flex-col">
          <select
            class="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            v-model="searchBy">
            <option value="Service Name">Review Title</option>
            <option value="Service Description">Description</option>
          </select> 
        </div>
        <div class="flex flex-col col-sm" v-if="searchBy === 'Service Name'">
          <label class="block">
            <input
              type="text"
              class="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              v-model="serviceName"
              v-on:keyup.enter="handleSubmitForm"
              placeholder="Enter Service Name"
            />
          </label>
        </div>
        <!-- Displays Service Description search field -->
        <div class="flex flex-col" v-if="searchBy === 'Service Description'">
          <input
            class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            type="text"
            v-model="serviceDescription"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter Service Description"
          />
        </div>
        <div class="flex flex-col">
          <button 
            class="mr-15 bg-red-700 text-white rounded"
            @click="handleSubmitForm" 
            type="submit">
            Search Review
          </button>
          <button
            class="mr-10 border border-red-700 bg-white text-red-700 rounded"
            @click="clearSearch"
            type="submit"
          >
            Clear Search
          </button>
        </div>
        
        
      </div>
      <div></div>
      <div></div>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10"
      >
      </div>
    </div>

    <hr class="mt-10 mb-10" />
    <!-- Display Found Data -->
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10"
    >
      <div class="ml-10">
        <h2 class="text-2xl font-bold">Current Reviews List Result</h2>
        <h3 class="italic">Click table row to edit/display an entry</h3>
      </div>
      <div class="flex flex-col col-span-2">
        <table class="min-w-full shadow-md rounded">
          <thead class="bg-gray-50 text-xl">
            <tr>
              <th class="p-4 text-left">Review Title</th>
              <th class="p-4 text-left">Check-in Status</th>
              <th class="p-4 text-left">Review Description</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-300">
            <tr
              @click="editService(service._id)"
              v-for="service in services"
              :key="service._id">
              <td class="p-2 text-left">{{ service.name }}</td>
              <td class="p-2 text-left">{{ service.status }}</td>
              <td class="p-2 text-left">{{ service.description }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>
