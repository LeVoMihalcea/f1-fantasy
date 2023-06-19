<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1>
      Hello World
    </h1>
    <h3>
      {{ msg }}
    </h3>
  </div>
</template>

<style scoped>
</style>
