<template>
    <h1>Races Page</h1>
    <table>
        <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Laps</th>
            <th>Fastest Lap</th>
        </tr>
        <tr v-for="race in races">
            <td>{{ race.id }}</td>
            <td>{{ race.name }}</td>
            <td>{{ race.laps }}</td>
            <td>{{ race.fastest_lap }}</td>
        </tr>
    </table>
</template>


<script setup>
import {onMounted, ref} from 'vue'

const races = ref([])
onMounted(async()=>{
    const response = await fetch('/api/races')
    races.value = await response.json()
    console.log(races)
})
</script>


<style scoped>
    table,h1{
        max-width: 600px;
        margin: 0 auto;
    }
</style>