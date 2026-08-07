<template>
  <div class="card shadow-sm">
    <div class="card-body p-0">

      <table class="table table-hover mb-0">

        <thead class="table-light">
          <tr>

            <th
              v-for="column in columns"
              :key="column.key"
            >
              {{ column.label }}
            </th>

            <th
              v-if="$scopedSlots.actions"
              class="text-center"
            >
              Actions
            </th>

          </tr>
        </thead>

        <tbody>

          <tr v-if="rows.length === 0">

            <td
              :colspan="columns.length + ($scopedSlots.actions ? 1 : 0)"
              class="text-center p-4"
            >

              No Records Found

            </td>

          </tr>

          <tr
            v-for="row in rows"
            :key="row.id"
          >

            <td
              v-for="column in columns"
              :key="column.key"
            >

              {{ row[column.key] }}

            </td>

            <td
              v-if="$scopedSlots.actions"
              class="text-center"
            >

              <slot
                name="actions"
                :row="row"
              />

            </td>

          </tr>

        </tbody>

      </table>

    </div>
  </div>
</template>

<script>

export default {

  name: 'DataTable',

  props: {

    columns: Array,

    rows: Array

  }

}

</script>
