<template>
    <h1>Drivers Page</h1>
    <table> 
        <tr>
            <th>Name</th>
            <th>Team</th>
            <th>Speed Rating</th>
        </tr>
        <tr v-for="driver in drivers">
            <td>{{ driver.name }}</td>
            <td>{{ driver.team }}</td>
            <td>{{ driver.speed_rating }}</td> 
        </tr>
    </table>
</template>


<script setup>
import { onMounted, ref } from 'vue';

const drivers = ref([])
onMounted(async () => {
    const response = await fetch('http://127.0.0.1:5000/drivers') 
    drivers.value = await response.json()
    console.log(drivers)
})
</script>


<style scoped>
    table,h1{
        max-width: 600px;
        margin: 0 auto;
    }
</style>