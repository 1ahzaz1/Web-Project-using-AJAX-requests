<template>
    <table class="table">
        <thead>
            <tr>
                <th>Person</th>
                <th>Motorbike</th>
                <th>Is Favourite Bike</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="ride in rides" :key="ride.id">
                <td>{{ ride.person__name || ride.person_name }}</td>
                <td>{{ ride.motorbike__name || ride.motorbike_name }}</td>
                <td>{{ ride.is_favourite ? "Yes" : "No" }}</td>
                <td>
                    <button @click="$emit('edit-ride', ride)" class="btn btn-sm btn-primary me-2">Edit</button>
                    <button @click="$emit('delete-ride', ride)" class="btn btn-sm btn-danger">Delete</button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        rides: {
            type: Array,
            required: true
        }
    }
};
</script>
