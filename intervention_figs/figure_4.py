
def plot_agreement_levels(questions_to_include, figure_size=(15, 9), pre_means=None, pre_group_means=None, post_group_means=None, title=None, use_full_statements=False, save=False, save_path="figs/latest.png"):
    fig, ax = plt.subplots(figsize=figure_size)

    x = range(1, len(questions_to_include) + 1)
    bar_width = 0.6
    
    # Filter pre_means for selected questions
    selected_pre_means = [pre_means[i-1] for i in questions_to_include]
    bars = ax.bar(x, selected_pre_means, color='lightblue', alpha=0.7, width=bar_width)

    # Define color palette explicitly
    groups = ['control', 'Russel', 'Joy', 'Aschenbrenner']
    colors = sns.color_palette("husl", n_colors=len(groups))

    # Calculate offsets for spreading out the points
    num_groups = len(groups)
    offsets = np.linspace(-bar_width/2 + bar_width/(num_groups*2), 
                          bar_width/2 - bar_width/(num_groups*2), 
                          num_groups)

    # Plot group means as scatter points with arrows
    for i, group in enumerate(groups):
        pre_group_means_row = pre_group_means.loc[group, [f'Q6_{q}' for q in questions_to_include]]
        post_group_means_row = post_group_means.loc[group, [f'Q16_{q}' for q in questions_to_include]]
        
        for j, q in enumerate(questions_to_include):
            x_pos = x[j] + offsets[i]
            ax.scatter(x_pos, pre_group_means_row[j], color=colors[i], s=50, zorder=3)
            dx = 0  # No horizontal change
            dy = post_group_means_row[j] - pre_group_means_row[j]
            ax.arrow(x_pos, pre_group_means_row[j], dx, dy, color=colors[i], 
                     width=0.005, head_width=0.05, head_length=0.05, 
                     zorder=2, length_includes_head=True)

    # Customize the plot
    ax.set_ylabel('Agreement Level', fontsize='medium')
    ax.set_xlabel('Statements', fontsize='medium')
    ax.set_title(title, fontsize='large')
    ax.set_xticks(x)
    if use_full_statements:
        ax.set_xticklabels([statements[i] for i in questions_to_include], rotation=45, ha='right')
    else:
        ax.set_xticklabels([f'S{i}' for i in questions_to_include])

    # Create legend with correct colors
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=group, 
                       markerfacecolor=color, markersize=10) 
                       for group, color in zip(groups, colors)]
    ax.legend(handles=legend_elements, title='Groups', fontsize='x-small', title_fontsize='small')

    # Set y-axis limits to accommodate arrows
    selected_pre_group_means = pre_group_means[[f'Q6_{q}' for q in questions_to_include]]
    selected_post_group_means = post_group_means[[f'Q16_{q}' for q in questions_to_include]]
    # y_min = min(selected_pre_group_means.min().min(), selected_post_group_means.min().min()) - 0.5
    # y_max = max(selected_pre_group_means.max().max(), selected_post_group_means.max().max()) + 0.5
    # ax.set_ylim(y_min, y_max)
    ax.set_ylim(1, 5)

    plt.tight_layout()
    if save:
        plt.savefig(save_path)
    plt.show()
