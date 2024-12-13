<template>
    <table class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Date of Birth</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="person in persons" :key="person.id">
                <td>{{ person.name }}</td>
                <td>{{ person.date_of_birth }}</td>
                <td>
                    <button @click="handleEdit(person)" class="btn btn-sm btn-primary me-2">Edit</button>
                    <button @click="$emit('delete-person', person)" class="btn btn-sm btn-danger">Delete</button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        persons: {
            type: Array,
            required: true
        }
    },
    methods: {
        handleEdit(person) {
            console.log('Edit clicked:', person);
            this.$emit('edit-person', person);
        }
    }
};
</script>