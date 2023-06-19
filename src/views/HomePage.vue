<template>
    <HelloWorld :msg="greetingFromHomePage"></HelloWorld>
</template>

<script setup lang="ts">
import HelloWorld from '@/components/HelloWorld.vue';
import { ref } from 'vue';

const greetingFromHomePage = ref('Hello from Home Page');

</script>