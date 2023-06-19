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
            <td>{{ computeFastestLapTime(race.fastest_lap) }}</td>
        </tr>
    </table>
</template>


<script setup lang="ts">
import {onMounted, ref} from 'vue'
import {formatDateToRaceTime} from '@/utils/timeUtils'
import type { Ref } from 'vue/dist/vue.js';

const races: Ref<any[]> = ref([])

onMounted(async()=>{
    const response = await fetch('/api/races')
    races.value = await response.json()
    console.log(races)
})

function computeFastestLapTime(fastestLapTime: string): string{
    return formatDateToRaceTime(new Date(fastestLapTime));
}
</script>


<style scoped>
    table,h1{
        max-width: 600px;
        margin: 0 auto;
    }
</style>