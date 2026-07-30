import 'package:flutter/material.dart';

class StatusUpdateScreen extends StatefulWidget {
  const StatusUpdateScreen({super.key});

  @override
  State<StatusUpdateScreen> createState() => _StatusUpdateScreenState();
}

class _StatusUpdateScreenState extends State<StatusUpdateScreen> {
  String status = 'Pending';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Update Status'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            DropdownButtonFormField<String>(
              value: status,
              items: const [
                DropdownMenuItem(
                  value: 'Pending',
                  child: Text('Pending'),
                ),
                DropdownMenuItem(
                  value: 'In Progress',
                  child: Text('In Progress'),
                ),
                DropdownMenuItem(
                  value: 'Resolved',
                  child: Text('Resolved'),
                ),
              ],
              onChanged: (value) {
                setState(() => status = value!);
              },
              decoration: const InputDecoration(
                labelText: 'Status',
                border: OutlineInputBorder(),
              ),
            ),

            const SizedBox(height: 24),

            SizedBox(
              width: double.infinity,
              height: 52,
              child: FilledButton(
                onPressed: () {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text('Status updated to $status'),
                    ),
                  );
                },
                child: const Text('Save'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}