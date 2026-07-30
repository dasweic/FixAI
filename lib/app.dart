import 'package:flutter/material.dart';
import 'core/routing/app_router.dart';
import 'core/theme/app_theme.dart';

class ThemeController {
  static final ValueNotifier<ThemeMode> mode =
      ValueNotifier(ThemeMode.system);
}

class FixAIApp extends StatelessWidget {
  const FixAIApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<ThemeMode>(
      valueListenable: ThemeController.mode,
      builder: (context, mode, _) {
        return MaterialApp.router(
          debugShowCheckedModeBanner: false,
          theme: AppTheme.light,
          darkTheme: AppTheme.dark,
          themeMode: mode,
          routerConfig: AppRouter.router,
        );
      },
    );
  }
}