import 'package:flutter/material.dart';

class AppError extends StatelessWidget {
  final String message;
  final VoidCallback? onRetry;

  const AppError({
    super.key,
    required this.message,
    this.onRetry,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Icon(Icons.error_outline, size: 72),
          const SizedBox(height: 16),
          Text(
            message,
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 16),
          if (onRetry != null)
            FilledButton(
              onPressed: onRetry,
              child: const Text('Retry'),
            ),
        ],
      ),
    );
  }
}