def save_legend_separately(groups, colors, blue_bar=False, figure_size=(3, 2), save_path='figs/legend.pdf'):
    """
    Create and save a standalone legend figure.
    
    Parameters:
    groups (list): List of group names
    colors (list): List of colors corresponding to groups
    blue_bar (bool): Whether to include the mean marker in legend
    figure_size (tuple): Size of the legend figure
    save_path (str): Path where to save the legend PDF
    """
    # Create a new figure for just the legend
    fig_legend = plt.figure(figsize=figure_size)
    ax = fig_legend.add_subplot(111)
    
    # Create legend elements
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=group, 
                                markerfacecolor=color, markersize=8) 
                      for group, color in zip(groups, colors)]
    
    if not blue_bar:
        legend_elements.append(plt.Line2D([0], [0], marker='_', color='black', 
                                        label='Mean', markersize=12))
    
    # Create legend
    ax.legend(handles=legend_elements, title='Preferred Timelines', fontsize=12, 
             title_fontsize=13, loc='center')
    
    # Turn off axis
    ax.axis('off')
    
    # Save legend with tight layout
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()

# Modified main plotting function to optionally skip legend
def plot_agreement_levels(questions_to_include, figure_size=(10, 7), pre_means=None, pre_group_means=None, 
                        post_group_means=None, title=None, use_full_statements=False, 
                        save_pdf=False, blue_bar=True, include_legend=True):
    plt.rcParams.update({'font.size': 12})
    
    fig, ax = plt.subplots(figsize=figure_size)

    x = range(1, len(questions_to_include) + 1)
    bar_width = 0.6

    total_means = pre_means[questions_to_include]
    total_stds = df[questions_to_include].std()

    if blue_bar:
        bars = ax.bar(x, total_means, color='lightblue', alpha=0.7, width=bar_width, 
                     yerr=total_stds, capsize=5, zorder=1)
    else:
        ax.errorbar(x, total_means, yerr=total_stds, fmt='_', color='black', 
                   markersize=12, capsize=5, capthick=1.5, zorder=1)

    groups = ['ASAP', 'Soon', 'Eventually', 'Never']
    colors = sns.color_palette("Set2", n_colors=len(groups))

    num_groups = len(groups)
    offsets = np.linspace(bar_width/2 - bar_width/(num_groups*2),
                         -bar_width/2 + bar_width/(num_groups*2),
                         num_groups)

    for i, group in enumerate(groups):
        pre_group_means_row = pre_group_means.loc[group, questions_to_include]
        group_stds = df[df['Q1'] == group][questions_to_include].std()
        
        for j in range(len(questions_to_include)):
            x_pos = x[j] + offsets[i]
            ax.errorbar(x_pos, pre_group_means_row[j], yerr=group_stds[j], 
                       fmt='o', color=colors[i], capsize=5, capthick=1.5,
                       markersize=8, zorder=2)

    ax.set_ylabel('Agreement Level (1-5 Scale)', fontsize=14, labelpad=10)
    ax.set_xlabel('Statement Number', fontsize=14, labelpad=10)
    if title:
        ax.set_title(title, fontsize=16, pad=20)
    ax.set_xticks(x)
    if use_full_statements:
        ax.set_xticklabels([statements[i] for i in questions_to_include], rotation=45, ha='right')
    else:
        ax.set_xticklabels([f'S{i[-1]}' for i in questions_to_include])

    # Only add legend if include_legend is True
    if include_legend:
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=group, 
                                    markerfacecolor=color, markersize=8) 
                          for group, color in zip(groups, colors)]
        
        if not blue_bar:
            legend_elements.append(plt.Line2D([0], [0], marker='_', color='black', 
                                            label='Mean', markersize=12))
        
        ax.legend(handles=legend_elements, title='Groups', fontsize=12, 
                 title_fontsize=13, bbox_to_anchor=(1.02, 1), loc='upper left')

    ax.set_ylim(0.8, 5.2)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    plt.tight_layout()
    
    if save_pdf:
        plt.savefig(f'figs/{title}.pdf', bbox_inches='tight', dpi=300)
    plt.show()
    
    # Save legend separately if requested
    if save_pdf:
        save_legend_separately(groups, colors, blue_bar, save_path=f'figs/{title}_legend.pdf')