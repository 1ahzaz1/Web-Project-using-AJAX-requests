<template>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Name</th>
                <th>Engine Capacity</th>
                <th>Description</th>
                <th>Automatic</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="motorbike in motorbikes" :key="motorbike.id">
                <td>{{ motorbike.name }}</td>
                <td>{{ motorbike.engine_capacity }}</td>
                <td>{{ motorbike.description }}</td>
                <td>
                    <i v-if="motorbike.is_automatic" class="bi bi-check-lg text-success"></i>
                    <i v-else class="bi bi-x-lg text-danger"></i>
                </td>
                <td>
                    <button class="btn btn-primary btn-sm me-2" @click="$emit('edit-motorbike', motorbike)">
                        <i class="bi bi-pencil"></i> Edit
                    </button>
                    <button class="btn btn-danger btn-sm" @click="$emit('delete-motorbike', motorbike)">
                        <i class="bi bi-trash"></i> Delete
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        motorbikes: {
            type: Array,
            required: true
        }
    },
    emits: ['delete-motorbike', 'edit-motorbike']
}
</script>